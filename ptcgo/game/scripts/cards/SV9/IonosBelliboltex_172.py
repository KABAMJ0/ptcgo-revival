from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd0ff55a-317b-5e3d-80dc-6584a7928e3e",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosBelliboltex.Name",
    display_name="Iono's Bellibolt ex",
    searchable_by=["Iono's Bellibolt ex", "Stage 1", "ex", "IonosBelliboltex"],
    subtypes=["Stage 1", "ex"],
    collector_number=172,
    set_code="SV9",
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