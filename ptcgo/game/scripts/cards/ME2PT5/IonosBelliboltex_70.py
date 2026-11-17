from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="148543e3-9938-52bc-8be6-e43b3d0bf991",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosBelliboltex.Name",
    display_name="Iono's Bellibolt ex",
    searchable_by=["Iono's Bellibolt ex", "Stage 1", "ex", "IonosBelliboltex"],
    subtypes=["Stage 1", "ex"],
    collector_number=70,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosTadbulb.Name",
    family_id=938,
    abilities=[
        Ability(
            title="Electric Streamer",
            game_text="As often as you like during your turn, you may attach a Basic Lightning Energy card from your hand to 1 of your Iono's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Thunderous Bolt",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=unimplemented,
        ),
    ],
)