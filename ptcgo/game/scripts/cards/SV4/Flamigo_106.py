from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f35c9970-1dd4-5f9d-acb7-db8381be0adf",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name",
    display_name="Flamigo",
    searchable_by=["Flamigo", "Basic", "Flamigo"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=973,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Combat Beak",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), 20, base=20),
        ),
    ],
)