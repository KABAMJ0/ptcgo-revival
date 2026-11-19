from ptcgo.game.card_effects.support_common import shuffle_hand_into_deck_draw
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack

card = PokemonCardDef(
    guid="2de9cd74-e6fc-5508-8eae-94a2a5cf54d0",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrampaGX.Name",
    display_name="Drampa-GX",
    searchable_by=["Drampa-GX", "Basic", "GX", "DrampaGX"],
    subtypes=["Basic", "GX"],
    collector_number=142,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=780,
    abilities=[
        Attack(
            title="Righteous Edge",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=discard_opponent_energy_attack(1, special_only=True),
        ),
        Attack(
            title="Berserk",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Big Wheel-GX",
            game_text="Shuffle your hand into your deck. Then, draw 10 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=shuffle_hand_into_deck_draw(10),
        ),
    ],
)