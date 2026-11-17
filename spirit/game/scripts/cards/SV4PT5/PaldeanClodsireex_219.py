from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9c1c3475-f8b4-5cfc-87b0-65e9100ca9a3",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsireex.Name",
    display_name="Paldean Clodsire ex",
    searchable_by=["Paldean Clodsire ex", "Stage 1", "ex", "PaldeanClodsireex"],
    subtypes=["Stage 1", "ex"],
    collector_number=219,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    family_id=194,
    abilities=[
        Ability(
            title="Toxic Wetland",
            game_text="Once during your turn, if a Stadium is in play, you may make your opponent's Active Pok\u00e9mon Poisoned.",
            effect=unimplemented,
        ),
        Attack(
            title="Needle Bone",
            game_text="Flip a coin. If tails, during your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=unimplemented,
        ),
    ],
)