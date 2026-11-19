from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import gust_attack


def _opponent_has_bench(board, player_id, pokemon=None):
    for pid in board.player_ids:
        if pid != player_id:
            bench = board.find_player_area(pid, "bench")
            return bench is not None and bool(bench.children)
    return False


async def fascinate(ctx):
    """On heads switch 1 of their Benched Pokemon with their Active."""
    await flip_gate(then=gust_attack(damage_before=0))(ctx)

card = PokemonCardDef(
    guid="d62905e2-634c-5faa-b434-f7115094ff29",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPersian.Name",
    display_name="Dark Persian",
    searchable_by=["Dark Persian", "Stage 1", "DarkPersian"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
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
            title="Fascinate",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Benched Pok\u00e9mon and switch it with the Defending Pok\u00e9mon. This attack can't be used if your opponent has no Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=_opponent_has_bench,
            effect=fascinate,
        ),
        Attack(
            title="Poison Claws",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)