from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import random_card_to_deck

card = PokemonCardDef(
    guid="ec32a305-da81-5962-9ccf-88cee9a4be19",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=479,
    abilities=[
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Electric Mischief",
            game_text="Flip 3 coins. For each heads, choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=random_card_to_deck(),
        ),
    ],
)