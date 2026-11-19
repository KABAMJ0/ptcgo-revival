from ptcgo.game.card_effects.support_common import discard_then_draw
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cc378757-79ec-5d80-8dae-7e31aca4cf31",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DedenneGX.Name",
    display_name="Dedenne-GX",
    searchable_by=["Dedenne-GX", "Basic", "GX", "DedenneGX"],
    subtypes=["Basic", "GX"],
    collector_number=195,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=702,
    abilities=[
        Ability(
            title="Dedechange",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard your hand and draw 6 cards. You can't use more than 1 Dedechange Ability each turn.",
            trigger=Triggers.ON_PLAY,
            effect=discard_then_draw(discard_count=99, draw_count=6, whole_hand=True),
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Tingly Return-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed. Put this Pok\u00e9mon and all cards attached to it into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)