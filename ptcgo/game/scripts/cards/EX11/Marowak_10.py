from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.patterns import is_pokemon_of_type


async def _energy_bone(ctx):
    """Choose up to one opponent Pokemon per Energy attached to Marowak; each
    chosen Pokemon takes 20 damage."""
    if ctx.attacker is None:
        return
    limit = len(ctx.attached_energies(ctx.attacker))
    targets = ctx.opponent_pokemon_in_play()
    if limit <= 0 or not targets:
        return
    picked = await ctx.choose_cards(
        targets, min(limit, len(targets)), minimum=1,
        prompt="Choose Pokémon to take 20 damage")
    for pokemon in picked:
        await ctx.deal_damage(20, target=pokemon)


def _defender_is_metal(ctx) -> bool:
    return ctx.defender is not None and is_pokemon_of_type(ctx.defender, "metal")


card = PokemonCardDef(
    guid="058a7e77-5f89-509d-971f-1169c4714fb6",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak δ",
    searchable_by=["Marowak \u03b4", "Stage 1", "Marowak"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Energy Bone",
            game_text="Choose a number of your opponent's Pok\u00e9mon up to the amount of Energy attached to Marowak. This attack does 20 damage to each of them.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            effect=_energy_bone,
        ),
        Attack(
            title="Metal Crusher",
            game_text="If the Defending Pok\u00e9mon is Metal Pok\u00e9mon, this attack's base damage is 90.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=bonus_if(_defender_is_metal, 40, base=50),
        ),
    ],
)