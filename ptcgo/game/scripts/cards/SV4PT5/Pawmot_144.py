from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4bebd006-755e-5052-95c3-95f265b79f3b",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name",
    display_name="Pawmot",
    searchable_by=["Pawmot", "Stage 2", "Pawmot"],
    subtypes=["Stage 2"],
    collector_number=144,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=921,
    abilities=[
        Ability(
            title="Electrogenesis",
            game_text="Once during your turn, you may search your deck for a Basic Lightning Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Electro Paws",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=unimplemented,
        ),
    ],
)