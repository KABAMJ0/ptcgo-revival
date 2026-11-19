from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.passives_common import Passive
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

class _HeavyweightPassive(Passive):
    """+2 retreat for THIS Muk while it holds a Grass Energy; the carrier
    identity check keeps a second Muk in play from taxing the first."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board) -> int:
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if not any(energy_provides_type(e, PokemonTypes.GRASS.value)
                   for e in board.attached_energies(pokemon)):
            return cost
        return cost + 2


async def _burning_sludge(ctx):
    await ctx.deal_damage()
    grass = count_energy("self", PokemonTypes.GRASS)(ctx)
    heads = await ctx.flip_coins(grass, "Burning Sludge") if grass else []
    if any(heads):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)

card = PokemonCardDef(
    guid="02a2e1ab-ddcd-5566-8c6c-4f783044e133",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Heavyweight",
            game_text="As long as there is a Grass Energy attached to Muk, you must pay an additional ColorlessColorless to retreat it.",
            passive=_HeavyweightPassive(),
        ),
        Attack(
            title="Burning Sludge",
            game_text="Flip a number of coins equal to the amount of Grass Energy attached to Muk. If any of them are heads, the Defending Pok\u00e9mon is now Poisoned and Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=_burning_sludge,
        ),
    ],
)
