from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.attacks_common import bonus_if


def _deck_has_few_cards(ctx) -> bool:
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    return deck is not None and len(deck.children) <= 3


card = PokemonCardDef(
    guid="b8ad65cb-9667-5bea-a7ac-fc55f65041d3",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orthworm.Name",
    display_name="Orthworm",
    searchable_by=["Orthworm", "Basic", "Orthworm"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=968,
    abilities=[
        Attack(
            title="Punch and Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=draw_attack(2),
        ),
        Attack(
            title="Crunch-Time Rush",
            game_text="If there are 3 or fewer cards in your deck, this attack does 150 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=bonus_if(_deck_has_few_cards, 150),
        ),
    ],
)