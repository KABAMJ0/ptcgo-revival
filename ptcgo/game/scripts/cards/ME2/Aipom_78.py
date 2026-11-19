from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import random_card_to_deck

card = PokemonCardDef(
    guid="ea68293c-d05e-5040-be2a-01bb3a7caf37",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic", "Aipom"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="ME2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Choose a random card from your opponent's hand, and your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=random_card_to_deck(),
        ),
    ],
)