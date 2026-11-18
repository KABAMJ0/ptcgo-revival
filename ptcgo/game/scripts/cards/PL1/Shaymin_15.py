from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="566c42f3-6921-5ac1-a447-3e8547f94f6f",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=492,
    abilities=[
        Attack(
            title="Growth",
            game_text="Attach a Grass Energy card from your hand to Shaymin.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Air Slash",
            game_text="Flip a coin. If tails, discard an Energy attached to Shaymin.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)