from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import gust_attack


async def tempt(ctx):
    """On heads, switch 1 of the opponent's Benched Pokemon with their Active -
    only when they have a Bench at all."""
    if not ctx.opponent_bench():
        return
    await flip_gate(then=gust_attack())(ctx)

card = PokemonCardDef(
    guid="715e6d95-7aef-565b-923c-7ca3979c47fa",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPersian.Name",
    display_name="Dark Persian",
    searchable_by=["Dark Persian", "Stage 1", "DarkPersian"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Tempt",
            game_text="If your opponent has any Benched Pok\u00e9mon, flip a coin. If heads, choose 1 of your opponent's Benched Pok\u00e9mon and switch it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tempt,
        ),
        Attack(
            title="Poison Claws",
            game_text="Flip a coin. if heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)