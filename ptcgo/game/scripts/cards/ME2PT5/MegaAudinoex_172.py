from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d274bba8-a07a-5325-a481-15c939461cd7",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaAudinoex.Name",
    display_name="Mega Audino ex",
    searchable_by=["Mega Audino ex", "Basic", "MEGA", "ex", "MegaAudinoex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=172,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Kaleidowaltz",
            game_text="Flip 3 coins. For each heads, search your deck for up to 2 Basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Ear Force",
            game_text="This attack does 80 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)