from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.patterns import is_pokemon_of_type

card = PokemonCardDef(
    guid="395d6a4f-f418-5736-8e30-7e76d431d16e",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=226,
    abilities=[
        Attack(
            title="Group Swim",
            game_text="Search your deck for a Water Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(
                lambda card: is_pokemon_of_type(card, "water"),
                count=1,
                reveal=True,
            ),
        ),
        Attack(
            title="Aqua Slash",
            game_text="Mantine can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)