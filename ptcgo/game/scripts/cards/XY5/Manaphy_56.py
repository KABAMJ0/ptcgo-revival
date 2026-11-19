from ptcgo.game.card_effects.support_common import shuffle_hand_into_deck_draw
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d919bf7e-5bba-5392-8180-23395a18f296",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=490,
    abilities=[
        Attack(
            title="Deep Sea Swirl",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=shuffle_hand_into_deck_draw(6),
        ),
        Attack(
            title="Life Saver",
            game_text="Put 2 Water Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
    ],
)