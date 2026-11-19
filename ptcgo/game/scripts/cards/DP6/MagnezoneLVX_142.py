from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import Activations
from ptcgo.game.attributes import SpecialConditions, AttrID
from ptcgo.game.session.effects import full_stack
from ptcgo.game.session.passives import carrier_pokemon


async def _electric_trans(ctx):
    """Electric Trans: move Lightning/Metal Energy between your Pokemon."""
    await ctx.move_energy_freely(
        ctx.my_pokemon_in_play(), ctx.my_pokemon_in_play(),
        predicate=lambda e: (energy_provides_type(e, PokemonTypes.LIGHTNING.value)
                             or energy_provides_type(e, PokemonTypes.METAL.value)),
        max_count=None, prompt="Choose a Lightning or Metal Energy")


async def _cyber_shock(ctx):
    """Cyber Shock: one Lightning and one Metal off Magnezone, then Paralyze."""
    await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda e: energy_provides_type(e, PokemonTypes.LIGHTNING.value),
        prompt="Discard a Lightning Energy")
    await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda e: energy_provides_type(e, PokemonTypes.METAL.value),
        prompt="Discard a Metal Energy")
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)

card = PokemonCardDef(
    guid="6d5fe875-7551-5ef8-b917-18078ccd2969",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneLVX.Name",
    display_name="Magnezone LV.X",
    searchable_by=["Magnezone LV.X", "Level-Up", "MagnezoneLVX"],
    subtypes=["Level-Up"],
    collector_number=142,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    family_id=462,
    abilities=[
        Ability(
            title="Electric Trans",
            game_text="As often as you like during your turn (before your attack), you may move a Lightning or Metal Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Magnezone is affected by a Special Condition.",
                        activation=Activations.UNLIMITED,
                        condition=lambda board, player_id, pokemon: not pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS),
            effect=_electric_trans,
        ),
        Attack(
            title="Cyber Shock",
            game_text="Discard a Lightning Energy and a Metal Energy attached to Magnezone. The Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1},
            damage=80,
            effect=_cyber_shock,
        ),
    ],
)