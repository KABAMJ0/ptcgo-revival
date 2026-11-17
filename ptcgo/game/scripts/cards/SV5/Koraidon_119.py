from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df04d52a-7a00-592a-9573-ceb115498ecd",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic", "Ancient", "Koraidon"],
    subtypes=["Basic", "Ancient"],
    collector_number=119,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=1007,
    abilities=[
        Attack(
            title="Primordial Beatdown",
            game_text="This attack does 30 damage for each of your Ancient Pok\u00e9mon in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)