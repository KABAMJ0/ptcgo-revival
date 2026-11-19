from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="48c7ac72-a932-5bea-a33f-39cb000dc291",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Ability(
            title="Acid Sampler",
            game_text="As long as Victreebel is your Active Pok\u00e9mon, put 1 damage counter on each Defending Pok\u00e9mon between turns. Acid Sampler stops working if your other Active Pok\u00e9mon is not a Victreebel.",
            effect=unimplemented,
        ),
        Attack(
            title="Acid",
            game_text="The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=no_retreat_attack(),
        ),
    ],
)