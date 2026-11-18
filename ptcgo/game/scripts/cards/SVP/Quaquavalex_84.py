from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d7079e75-f90e-53c6-8166-b3e11a8c75ce",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaquavalex.Name",
    display_name="Quaquaval ex",
    searchable_by=["Quaquaval ex", "Stage 2", "ex", "Quaquavalex"],
    subtypes=["Stage 2", "ex"],
    collector_number=84,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    family_id=912,
    abilities=[
        Attack(
            title="Exciting Dance",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, switch out your opponent's Active Pok\u00e9mon to the Bench.\u00a0(Your opponent chooses the new Active Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Shot",
            game_text="Put 2 Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=unimplemented,
        ),
    ],
)