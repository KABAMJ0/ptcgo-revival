from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_hand


def _fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def heat_assist(ctx):
    """Attach up to 3 Fire Energy from your hand to your Pokemon in any way."""
    await attach_from_hand(_fire_energy, count=3, distribute=True, minimum=0,
                           prompt="Choose up to 3 Fire Energy to attach")(ctx)

card = PokemonCardDef(
    guid="fa48510e-6146-5674-9c87-0778335176a2",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1", "Darmanitan"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Heat Assist",
            game_text="Attach up to 3 Fire Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            effect=heat_assist,
        ),
        Attack(
            title="Darmani-Hands",
            game_text="Flip 4 coins. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=4, bonus_per_heads=50),
        ),
    ],
)