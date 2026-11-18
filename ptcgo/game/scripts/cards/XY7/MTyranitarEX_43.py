from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6a1ea7e2-d424-53c0-b605-0dc540e1cdb8",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MTyranitarEX.Name",
    display_name="M Tyranitar-EX",
    searchable_by=["M Tyranitar-EX", "MEGA", "EX", "MTyranitarEX"],
    subtypes=["MEGA", "EX"],
    collector_number=43,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=240,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TyranitarEX.Name",
    family_id=248,
    abilities=[
        Attack(
            title="Destroyer King",
            game_text="This attack does 60 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)