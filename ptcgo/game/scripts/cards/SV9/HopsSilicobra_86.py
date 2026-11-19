from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_stadium_card
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="b5945090-2b62-515d-ad53-3c59da5a9458",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSilicobra.Name",
    display_name="Hop's Silicobra",
    searchable_by=["Hop's Silicobra", "Basic", "HopsSilicobra"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=843,
    abilities=[
        Attack(
            title="Turf Maker",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_stadium_card, count=1, minimum=1, reveal=True),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)