from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c0c20356-6761-5504-a47d-7662461bc04c",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirockex.Name",
    display_name="Regirock ex",
    searchable_by=["Regirock ex", "Basic", "ex", "Regirockex"],
    subtypes=["Basic", "ex"],
    collector_number=107,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Attack(
            title="Regi Charge",
            game_text="Attach up to 2 Basic Fighting Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Giant Rock",
            game_text="If your opponent's Active Pok\u00e9mon is a Stage 2 Pok\u00e9mon, this attack does 140 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=140,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)