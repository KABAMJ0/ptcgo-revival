from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb2aa3eb-262d-50c6-bcab-e35f6d093496",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walreinex.Name",
    display_name="Walrein ex",
    searchable_by=["Walrein ex", "Stage 2", "ex", "Walreinex"],
    subtypes=["Stage 2", "ex"],
    collector_number=99,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    family_id=363,
    abilities=[
        Ability(
            title="Chilling Breath",
            game_text="Once during your turn, when you play Walrein ex from your hand to evolve 1 of your Pok\u00e9mon, you may use this power. Your opponent can't play any Trainer cards from his or her hand during your opponent's next turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Wreck",
            game_text="If there is any Stadium card in play, this attack does 70 damage plus 20 more damage. Discard that Stadium card.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)