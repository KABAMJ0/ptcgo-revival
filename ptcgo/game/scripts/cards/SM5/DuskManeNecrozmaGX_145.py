from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, condition_attack

def _behind_on_prizes(board, player_id, pokemon=None):
    mine = board.find_player_area(player_id, "prizePile")
    other = next((p for p in board.player_ids if p != player_id), None)
    theirs = board.find_player_area(other, "prizePile")
    return bool(mine and theirs and len(mine.children) > len(theirs.children))


card = PokemonCardDef(
    guid="bbc325b2-a9cd-5a4f-828d-3d9bddb34556",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuskManeNecrozmaGX.Name",
    display_name="Dusk Mane Necrozma-GX",
    searchable_by=["Dusk Mane Necrozma-GX", "Basic", "GX", "Ultra Beast", "DuskManeNecrozmaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=145,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="Meteor Tempest",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=self_energy_discard_attack(count=3),
        ),
        Attack(
            title="Sun's Eclipse-GX",
            game_text="You can use this attack only if you have more Prize cards remaining than your opponent. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 3},
            damage=250,
            condition=_behind_on_prizes,
            effect=condition_attack(),
        ),
    ],
)