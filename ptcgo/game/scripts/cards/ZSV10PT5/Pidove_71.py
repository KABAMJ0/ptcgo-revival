from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01d66967-8bd0-5de5-b3a1-f022055edf39",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    display_name="Pidove",
    searchable_by=["Pidove", "Basic", "Pidove"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=519,
    abilities=[
        Attack(
            title="Scout",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Stampede",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)