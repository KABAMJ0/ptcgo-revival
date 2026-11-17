from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1e685545-8520-5d19-8e9b-dfb9fe283b4c",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Irritating Buzz",
            game_text="As long as Flygon is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Active Pok\u00e9mon between turns, excluding Fighting Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Sand Sonic",
            game_text="If you attach a Fighting Energy card from your hand to Flygon during this turn, this attack does 60 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)