from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9ad2de70-83a2-5c6b-a511-6beea227a7a9",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=312,
    abilities=[
        Ability(
            title="Buddy Pulse",
            game_text="If you have Plusle in play, whenever your opponent attaches an Energy card from their hand to 1 of their Pok\u00e9mon, put 2 damage counters on that Pok\u00e9mon. The effect of Buddy Pulse doesn't stack.",
            effect=unimplemented,
        ),
        Attack(
            title="Speed Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)