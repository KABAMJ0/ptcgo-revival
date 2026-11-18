from ptcgo.game.card_effects.passives_common import draw_when_damaged_with_weakness
from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="b2d1d8e8-308a-59cd-a63a-1cf37fc28c6f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdversityPolicy.Name",
    display_name="Adversity Policy",
    searchable_by=["Adversity Policy", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=74,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Adversity Policy",
            game_text="If the Pok\u00e9mon this card is attached to has Weakness to your opponent's Active Pok\u00e9mon's type, is in the Active Spot, and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), draw 3 cards.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=draw_when_damaged_with_weakness,
        ),
    ],
)
