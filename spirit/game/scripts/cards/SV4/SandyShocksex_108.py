from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7623fd43-4828-5538-9c90-9566f51f19f3",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandyShocksex.Name",
    display_name="Sandy Shocks ex",
    searchable_by=["Sandy Shocks ex", "Basic", "ex", "Ancient", "SandyShocksex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=108,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=989,
    abilities=[
        Ability(
            title="Magnetic Absorption",
            game_text="Once during your turn, if your opponent has 4 or fewer Prize cards remaining, you may attach a Basic Fighting Energy card from your discard pile to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Earthen Spike",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)