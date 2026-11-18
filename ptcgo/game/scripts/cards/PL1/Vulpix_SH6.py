from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import basic_energy_of

card = PokemonCardDef(
    guid="a2523f97-5dd6-53f5-b3ee-cf1719bc6137",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name="Vulpix",
    searchable_by=["Vulpix", "Basic", "Vulpix"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Find Wildfire",
            game_text="Search your deck for up to 2 Fire Energy cards, show them to your opponent, and put them in your hand. Shuffle your deck afterward.",
            cost={},
            effect=search_to_hand(basic_energy_of("fire"), count=2, reveal=True),
        ),
        Attack(
            title="Brushfire",
            game_text="Does 10 damage to each of your opponent's Benched Grass Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Inflame",
            game_text="Discard a Fire Energy card from your hand. (If you can't discard a card from your hand, this attack does nothing.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)