from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="23745c99-ed21-5a35-b83b-3f2fffc83eae",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoex.Name",
    display_name="Tapu Koko ex",
    searchable_by=["Tapu Koko ex", "Basic", "ex", "TapuKokoex"],
    subtypes=["Basic", "ex"],
    collector_number=222,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=785,
    abilities=[
        Attack(
            title="Vengeful Shock",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage, and your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Extreme Current",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)