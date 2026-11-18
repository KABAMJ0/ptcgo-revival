from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.trainers import is_energy_card
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="90e1a38b-4107-577b-afdb-a4b96e52127f",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1", "Heliolisk"],
    subtypes=["Stage 1"],
    collector_number=155,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Attack(
            title="Parabolic Charge",
            game_text="Search your deck for up to 4 Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_energy_card, count=4, reveal=True),
        ),
        Attack(
            title="Electroslug",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)