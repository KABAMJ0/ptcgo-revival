from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
card = PokemonCardDef(
    guid="5d55f30a-0ee5-5884-8fd9-646468a5fafb",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=716,
    abilities=[
        Attack(
            title="Geo Storm",
            game_text="This attack does 30 damage for each Psychic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_energy("mine", energy_type=PokemonTypes.PSYCHIC), 30),
        ),
    ],
)