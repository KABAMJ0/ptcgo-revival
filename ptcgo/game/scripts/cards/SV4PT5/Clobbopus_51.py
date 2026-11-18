from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="579d5e3f-2e8f-5d19-9d02-736bf68be9de",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    display_name="Clobbopus",
    searchable_by=["Clobbopus", "Basic", "Clobbopus"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV4PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=852,
    abilities=[
        Attack(
            title="Feint",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)