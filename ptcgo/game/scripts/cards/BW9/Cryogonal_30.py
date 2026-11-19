from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import pokemon_of
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="36a18b62-338a-5b75-9b8b-d75c6db60f44",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal", "Basic", "Team Plasma", "Cryogonal"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=30,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=615,
    abilities=[
        Attack(
            title="Call Sign",
            game_text="Search your deck for a Water Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(pokemon_of("water"), count=1, minimum=1, reveal=True),
        ),
        Attack(
            title="Cryofreeze",
            game_text="Discard an Energy attached to this Pok\u00e9mon. The Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)