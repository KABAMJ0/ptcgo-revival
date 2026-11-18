from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4e1b681c-79cb-5ee2-816b-81a2ede63582",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMimikyu.Name",
    display_name="Team Rocket's Mimikyu",
    searchable_by=["Team Rocket's Mimikyu", "Basic", "TeamRocketsMimikyu"],
    subtypes=["Basic"],
    collector_number=238,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=778,
    abilities=[
        Attack(
            title="Gemstone Mimicry",
            game_text="Choose 1 of your opponent's Active Tera Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)