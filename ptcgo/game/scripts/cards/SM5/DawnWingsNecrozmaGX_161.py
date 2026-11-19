from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

def _behind_on_prizes(board, player_id, pokemon=None):
    mine = board.find_player_area(player_id, "prizePile")
    other = next((p for p in board.player_ids if p != player_id), None)
    theirs = board.find_player_area(other, "prizePile")
    return bool(mine and theirs and len(mine.children) > len(theirs.children))


card = PokemonCardDef(
    guid="94164ace-7d0e-52e6-ae45-c5c671b79a9c",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DawnWingsNecrozmaGX.Name",
    display_name="Dawn Wings Necrozma-GX",
    searchable_by=["Dawn Wings Necrozma-GX", "Basic", "GX", "Ultra Beast", "DawnWingsNecrozmaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=161,
    set_code="SM5",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=800,
    abilities=[
        Ability(
            title="Invasion",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may switch it with your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Dark Flash",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
        Attack(
            title="Moon's Eclipse-GX",
            game_text="You can use this attack only if you have more Prize cards remaining than your opponent. Prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=180,
            condition=_behind_on_prizes,
            effect=protect_next_turn(prevent=True, effects_too=True),
        ),
    ],
)