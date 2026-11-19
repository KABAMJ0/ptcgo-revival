from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

def _opponent_has_bench(board, player_id, pokemon=None):
    for pid in board.player_ids:
        if pid != player_id:
            bench = board.find_player_area(pid, "bench")
            return bench is not None and bool(bench.children)
    return False


card = PokemonCardDef(
    guid="8771c112-a6bb-513e-b95f-02ea4ad1b09a",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPersian.Name",
    display_name="Dark Persian",
    searchable_by=["Dark Persian", "Stage 1", "DarkPersian"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
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
            effect=flip_gate(then=gust_attack(damage_before=0)),
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