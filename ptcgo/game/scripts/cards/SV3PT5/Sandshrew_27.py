from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9618127-8c17-5071-9b1e-600826d4a6d1",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    display_name="Sandshrew",
    searchable_by=["Sandshrew", "Basic", "Sandshrew"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=27,
    abilities=[
        Ability(
            title="Sand Screen",
            game_text="Trainer cards in your opponent's discard pile can't be put into their deck by an effect of your opponent's Item or Supporter cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)