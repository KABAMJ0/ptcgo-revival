from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9f860c8-65ac-5742-bfd3-35a82c36218e",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidokingex.Name",
    display_name="Team Rocket's Nidoking ex",
    searchable_by=["Team Rocket's Nidoking ex", "Stage 2", "ex", "TeamRocketsNidokingex"],
    subtypes=["Stage 2", "ex"],
    collector_number=119,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidorino.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Tainted Horn",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During Pok\u00e9mon Checkup, put 8 damage counters on that Pok\u00e9mon instead of 1.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
        Attack(
            title="Kingly Impact",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
        ),
    ],
)