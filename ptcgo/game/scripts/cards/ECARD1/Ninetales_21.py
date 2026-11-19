from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


def _is_fire_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def _ethereal_flame(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 99, predicate=_is_fire_energy,
        prompt="Choose Fire Energy to discard from Ninetales")
    await ctx.deal_damage(30 + 20 * len(discarded))

card = PokemonCardDef(
    guid="d6af842d-d795-5f01-88ad-9e9e5da9a76b",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Mislead",
            game_text="Flip 2 coins. If either of them is heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True, coins=2, min_heads=1),
        ),
        Attack(
            title="Ethereal Flame",
            game_text="Discard all Fire Energy cards attached to Ninetales. This attack does 30 damage plus 20 more damage for each card discarded this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=_ethereal_flame,
        ),
    ],
)