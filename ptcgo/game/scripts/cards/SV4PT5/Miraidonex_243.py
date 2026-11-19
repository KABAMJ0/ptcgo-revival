from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack

card = PokemonCardDef(
    guid="81e40c77-6ef3-512d-909f-0278e2de6368",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex", "Basic", "ex", "Miraidonex"],
    subtypes=["Basic", "ex"],
    collector_number=243,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Ability(
            title="Tandem Unit",
            game_text="Once during your turn, you may search your deck for up to 2 Basic Lightning Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Photon Blaster",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=lock_self_attack(),
        ),
    ],
)