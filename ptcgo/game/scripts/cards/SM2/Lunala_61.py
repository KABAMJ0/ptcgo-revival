from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e2aca28c-ff91-5ea3-a54d-0c56211f8421",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name",
    display_name="Lunala",
    searchable_by=["Lunala", "Stage 2", "Lunala"],
    subtypes=["Stage 2"],
    collector_number=61,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=792,
    abilities=[
        Attack(
            title="Shatter Shot",
            game_text="This attack does 40 damage times the amount of Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            damage_operator="x",
            effect=damage_per(count_energy("self", PokemonTypes.PSYCHIC), 40),
        ),
        Attack(
            title="Wings of the Moone",
            game_text="Move all Energy from this Pok\u00e9mon to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)