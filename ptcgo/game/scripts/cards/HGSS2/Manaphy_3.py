from ptcgo.game.card_effects.support_common import shuffle_hand_into_deck_draw
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8cc27c2e-2be9-558d-bbda-d0bdd0aa2d41",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="HGSS2",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Attack(
            title="Deep Sea Swirl",
            game_text="Shuffle your hand into your deck. Then, draw 5 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=shuffle_hand_into_deck_draw(5),
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)