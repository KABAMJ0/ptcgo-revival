from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5d7a9dcf-fc97-5582-941b-9d4542493195",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV6PT5",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Attack(
            title="Power Charger",
            game_text="Search your deck for a Basic Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=search_attach_energy(predicate=is_basic_energy_card, count=1, to_self=True),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)