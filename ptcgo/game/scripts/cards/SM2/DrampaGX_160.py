from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d944aad2-ed2c-5c28-8864-f9328912087a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrampaGX.Name",
    display_name="Drampa-GX",
    searchable_by=["Drampa-GX", "Basic", "GX", "DrampaGX"],
    subtypes=["Basic", "GX"],
    collector_number=160,
    set_code="SM2",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=780,
    abilities=[
        Attack(
            title="Righteous Edge",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Berserk",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Big Wheel-GX",
            game_text="Shuffle your hand into your deck. Then, draw 10 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)