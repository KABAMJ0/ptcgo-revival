from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="90c1fa1a-e8f8-57de-bffd-49eb8eed985c",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaRayquazaex.Name",
    display_name="Mega Rayquaza ex",
    searchable_by=["Mega Rayquaza ex", "Basic", "MEGA", "ex", "MegaRayquazaex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=84,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Ability(
            title="Ruler's Roar",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand onto your Bench, you may use this Ability. Look at the top 4 cards of your deck and attach a Basic Energy card you find there to this Pok\u00e9mon. Shuffle the other cards and put them on the bottom of your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Storm Emerald",
            game_text="This attack does 50 damage for each Fire Energy and each Lightning Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)