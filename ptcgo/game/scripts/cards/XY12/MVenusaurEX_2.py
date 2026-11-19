from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4a5038a4-8c36-594c-b93f-b317d92b2520",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MVenusaurEX.Name",
    display_name="M Venusaur-EX",
    searchable_by=["M Venusaur-EX", "MEGA", "EX", "MVenusaurEX"],
    subtypes=["MEGA", "EX"],
    collector_number=2,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurEX.Name",
    family_id=3,
    abilities=[
        Attack(
            title="Crisis Vine",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=condition_attack(SpecialConditions.PARALYZED, SpecialConditions.POISONED),
        ),
    ],
)