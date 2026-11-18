from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9ddc1a5a-93fa-5b06-9b36-af909d101028",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCramorant.Name",
    display_name="Hop's Cramorant",
    searchable_by=["Hop's Cramorant", "Basic", "HopsCramorant"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=845,
    abilities=[
        Attack(
            title="Fickle Spitting",
            game_text="If your opponent doesn't have exactly 3 or 4 Prize cards remaining, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)