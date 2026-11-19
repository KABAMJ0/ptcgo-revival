from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="39b26a38-9784-588b-8419-9c185f397f0d",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    display_name="Skitty",
    searchable_by=["Skitty", "Basic", "Skitty"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="EX1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=300,
    abilities=[
        Attack(
            title="Plus Energy",
            game_text="Attach a basic Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_hand(is_basic_energy_card, count=1, target="choice"),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)